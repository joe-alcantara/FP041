set.seed(123)

data <- runif(n=1000, min=1.2, max=12)

hist(data, col='steelblue', main="Histogram of Turtle Shell Widths")

MEAN <- mean(data)
SD <- sd(data)

samplemean <- c()
samplesd <- c()
n=1000
for (i in 1:n){
  samplemean[i] = mean(sample(data, 5, replace=TRUE))
  samplesd[i] = sd(sample(data, 5, replace=TRUE))
}
mean(samplemean)
mean(samplesd)

hist(samplemean, col = 'red', xlab = 'Turtle Shell Widths', main='Sample size = 5')
hist(samplesd, col='yellow', xlab = 'Turtle Shell Widths', main='Sample size = 5')


samplemean <- c()
samplesd <- c()
n=1000
for (i in 1:n){
  samplemean[i] = mean(sample(data, 10, replace=TRUE))
  samplesd[i] = sd(sample(data, 10, replace=TRUE))
}
mean(samplemean)
mean(samplesd)

hist(samplemean, col = 'red', xlab = 'Turtle Shell Widths', main='Sample size = 10')
hist(samplesd, col='yellow', xlab = 'Turtle Shell Widths', main='Sample size = 10')

samplemean <- c()
samplesd <- c()
n=1000
for (i in 1:n){
  samplemean[i] = mean(sample(data, 30, replace=TRUE))
  samplesd[i] = sd(sample(data, 30, replace=TRUE))
}
mean(samplemean)
mean(samplesd)

hist(samplemean, col = 'red', xlab = 'Turtle Shell Widths', main='Sample size = 30')
hist(samplesd, col='yellow', xlab = 'Turtle Shell Widths', main='Sample size = 30')

samplemean <- c()
samplesd <- c()
n=1000
for (i in 1:n){
  samplemean[i] = mean(sample(data, 60, replace=TRUE))
  samplesd[i] = sd(sample(data, 60, replace=TRUE))
}
mean(samplemean)
mean(samplesd)

hist(samplemean, col = 'red', xlab = 'Turtle Shell Widths', main='Sample size = 60')
hist(samplesd, col='yellow', xlab = 'Turtle Shell Widths', main='Sample size = 60')




