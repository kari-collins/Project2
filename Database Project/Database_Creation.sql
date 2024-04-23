CREATE TABLE User (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(25) NOT NULL,
    Age INT,
    Email VARCHAR(60) UNIQUE NOT NULL,
    DietID INT,
    CuisineID INT,
    FOREIGN KEY (DietID) REFERENCES Diet(DietID),
    FOREIGN KEY (CuisineID) REFERENCES Cuisine(CuisineID)
);

CREATE TABLE Recipes (
    RecipeID INT AUTO_INCREMENT PRIMARY KEY,
    RecipeName VARCHAR(150),
    Cook_Time INT,
    Difficulty_Level INT,
    Nutritional_Info VARCHAR(255),
    Instructions VARCHAR(255),
    DietID INT,
    CuisineID INT,
    FOREIGN KEY (DietID) REFERENCES Diet(DietID),
    FOREIGN KEY (CuisineID) REFERENCES Cuisine(CuisineID)
);

CREATE TABLE Diet (
    DietID INT AUTO_INCREMENT PRIMARY KEY,
    Diet_Name VARCHAR(25) UNIQUE
);

CREATE TABLE Cuisine (
    CuisineID INT AUTO_INCREMENT PRIMARY KEY,
    Cuisine_Name VARCHAR(25) UNIQUE
);

CREATE TABLE Ingredients (
    IngredientID INT AUTO_INCREMENT PRIMARY KEY,
    Ingredient_Name VARCHAR(100),
    DietID INT,
    FOREIGN KEY (DietID) REFERENCES Diet(DietID)
);
