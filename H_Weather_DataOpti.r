# Complex Math Operations in R

# Define two complex numbers
z1 <- complex(real = 3, imaginary = 4)
z2 <- complex(real = 1, imaginary = 2)

# Addition
addition <- z1 + z2

# Subtraction
subtraction <- z1 - z2

# Multiplication
multiplication <- z1 * z2

# Division
division <- z1 / z2

# Modulus (Magnitude)
modulus_z1 <- Mod(z1)
modulus_z2 <- Mod(z2)

# Argument (Phase Angle)
argument_z1 <- Arg(z1)
argument_z2 <- Arg(z2)

# Conjugate
conjugate_z1 <- Conj(z1)
conjugate_z2 <- Conj(z2)

# Print results
cat("Addition: ", addition, "\n")
cat("Subtraction: ", subtraction, "\n")
cat("Multiplication: ", multiplication, "\n")
cat("Division: ", division, "\n")
cat("Modulus of z1: ", modulus_z1, "\n")
cat("Modulus of z2: ", modulus_z2, "\n")
cat("Argument of z1: ", argument_z1, "\n")
cat("Argument of z2: ", argument_z2, "\n")
cat("Conjugate of z1: ", conjugate_z1, "\n")
cat("Conjugate of z2: ", conjugate_z2, "\n")
