package main

import (
	"fmt"
	"math"
	"math/cmplx"
)

func main() {
	// Complex number operations
	c1 := complex(3, 4)
	c2 := complex(1, 2)

	sum := c1 + c2
	diff := c1 - c2
	prod := c1 * c2
	quot := c1 / c2

	fmt.Printf("Complex number operations:\n")
	fmt.Printf("Sum: %v\n", sum)
	fmt.Printf("Difference: %v\n", diff)
	fmt.Printf("Product: %v\n", prod)
	fmt.Printf("Quotient: %v\n", quot)

	// Trigonometric functions
	angle := math.Pi / 4
	sin := math.Sin(angle)
	cos := math.Cos(angle)
	tan := math.Tan(angle)

	fmt.Printf("\nTrigonometric functions:\n")
	fmt.Printf("Sin(π/4): %v\n", sin)
	fmt.Printf("Cos(π/4): %v\n", cos)
	fmt.Printf("Tan(π/4): %v\n", tan)

	// Exponential and logarithmic functions
	exp := math.Exp(1)
	log := math.Log(10)
	log10 := math.Log10(100)

	fmt.Printf("\nExponential and logarithmic functions:\n")
	fmt.Printf("Exp(1): %v\n", exp)
	fmt.Printf("Log(10): %v\n", log)
	fmt.Printf("Log10(100): %v\n", log10)

	// Complex exponential and logarithmic functions
	cmplxExp := cmplx.Exp(c1)
	cmplxLog := cmplx.Log(c1)

	fmt.Printf("\nComplex exponential and logarithmic functions:\n")
	fmt.Printf("Exp(3+4i): %v\n", cmplxExp)
	fmt.Printf("Log(3+4i): %v\n", cmplxLog)
}
