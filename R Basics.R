#This R code is regarding the basics of R programming 
#remove all the previous objects
rm(list=ls())
#Setting the working directory
setwd("D:/python & R/Kkamaljeet Singh (Data Scientist1)/Assignment")
#checking the current Set Directory
getwd()
#skipping the 2nd Row
df=read.csv("IMDB_data.csv",header=T)[-2,]
#Extraction of the Unique Genres 
unique(df $ Genre)
#counting the unique Genres
length(unique(df $ Genre))
#Creating the Data Frame
dat=data.frame(df)
#checking the structure of data type
str(dat)
#converting the required data types
dat$Plot = as.character(dat$Plot)
dat$imdbVotes = as.numeric(dat$imdbVotes)
dat$imdbRating = as.numeric(dat$imdbRating)
dat$Genre = as.character(dat$Genre)
dat$Year = as.numeric(dat$Year)
dat$Language = as.character(dat$Language)
#Checking the Structure of the new Data types
str(dat)
#sorting the Genre by its name
dat = dat[ order (dat $Genre),]
#Difference of IMDB rating and IMDB Votes  
sub = dat$imdbVotes-dat$imdbRating  
#Square of the New Variable
sub =sub*sub
#Creating the new variable named Difference
dat$Difference = with(dat,sub)
#Displaying the file with New variable
dat
#writing the output file in CSV Format
write.csv(dat,"IMDB_Data Output in R.csv",row.names = F)
