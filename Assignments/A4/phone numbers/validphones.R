library(tidyverse)
library(readxl)
library(httr)
library(jsonlite)


# import data
numbers <- read_xlsx("Phonesurvey.xlsx", skip = 2)

# set code
code <- '301'

# add code to the phone numbers and create valid column
numbers <- numbers %>%
    mutate(`Phone number` = paste(`code`,as.character(`Phone number`), sep ="")) %>%
    mutate(valid = FALSE, location = "", carrier ="", line_type = "")



# create validtest function
valid.test <- function(phone.no){
    base.url <- "http://apilayer.net/api/validate"
    key <- "e08a4d253c965038ecb004941c992507"
    info <- GET(url = paste(base.url,"?access_key=",key,"&number=",phone.no,"&country_code=US&format=1", sep=""))
    info_content <- content(info)
    return(info_content)
}

# call valid test function for each number and add values into df
# I decided to record the line type as well, out of curiosity

for (i in seq_along(numbers$`Phone number`)) {
    API.info <- valid.test(numbers$`Phone number`[i])
    numbers$valid[i] <- API.info$valid
    if (length(API.info$location) > 0 ){
        numbers$location[i] <- API.info$location
    }
    if (length(API.info$carrier) > 0 ){
        numbers$carrier[i] <- API.info$carrier
    }
    if (length(API.info$line_type) > 0 ){
    numbers$line_type[i] <- API.info$line_type
    }
}

# save the data as csv. You can opt to save as xlsx using the xlsx library
write_excel_csv(numbers, "ValidatedPhones2.csv")
