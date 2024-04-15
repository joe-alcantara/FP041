# Clear Workspace
rm(list=ls())

# Load Data
df  <- read.csv("C:/Users/joe/Downloads/automobile/imports-85.data", header=FALSE)

# Create column names
names <- c("symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
                       "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight", 
                       "engine-type", "num_of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio",
                       "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price")

# Rename columns
names(df) <- names

# Delete columns
df$`normalized-losses` <- NULL


# Delete any rows with missing values
df <- na.omit(df)

# Delete any rows with catagorical data
df$symboling <- NULL

# Remove unknown values
df <- df[which(df$`num-of-doors` != '?'),]
df <- df[which(df$price != '?'),]
df <- df[which(df$bore != '?'),]
df <- df[which(df$stroke != '?'),]
df <- df[which(df$horsepower != '?'),]

write.csv(df, "automobile.csv")

model = lm(price ~ `city-mpg` + `highway-mpg` + horsepower + make, data = df) #Create the linear regression
summary(model)

typeof(df$`city-mpg`)

df$horsepower <- as.integer(df$horsepower)
