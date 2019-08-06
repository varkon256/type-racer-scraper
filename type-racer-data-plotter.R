library(readr)
typingdata <- read_csv("output.csv")
head(typingdata)
race = typingdata$`Race #`
speed = typingdata$Speed
plot(speed ~ race,
     main = "Speed vs Number of Races",
     xlab = "Number of Races",
     ylab = "Speed",
     pch = 16, col = rgb(0, 0, 1, 0.6))

