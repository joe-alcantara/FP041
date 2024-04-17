rm(list=ls())

library(class)

# Load the dataset
data <- read.csv("C:/Users/joe/Downloads/breast+cancer+wisconsin+diagnostic/wdbc.data", header=FALSE)

# Set a random seed for reproducibility
set.seed(123)

# Split the data into 70% training and 30% testing
train_index <- sample(1:nrow(data), 0.7 * nrow(data))
train_data <- data[train_index, ]
test_data <- data[-train_index, ]

# Train the k-NN model
k <- 50  # Specify the number of neighbors (you can choose any value)
model <- knn(train = train_data[, 3:6], test = test_data[, 3:6], cl = train_data$V2, k = k)

# Evaluate the model
accuracy <- mean(model == test_data$V2) * 100
cat("Accuracy:", accuracy, "%\n")


