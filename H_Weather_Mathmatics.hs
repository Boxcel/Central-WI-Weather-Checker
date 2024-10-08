module WeatherMathematics where

-- Function to calculate the roots of a quadratic equation ax^2 + bx + c = 0
quadraticRoots :: (Floating a, Ord a) => a -> a -> a -> (a, a)
quadraticRoots a b c
    | discriminant < 0 = error "Complex roots"
    | otherwise = ((-b + sqrt discriminant) / (2 * a), (-b - sqrt discriminant) / (2 * a))
  where
    discriminant = b * b - 4 * a * c

-- Function to multiply two matrices
type Matrix a = [[a]]

matrixMultiply :: Num a => Matrix a -> Matrix a -> Matrix a
matrixMultiply a b
    | null a || null (head a) || null b || null (head b) = error "Empty matrix"
    | length (head a) /= length b = error "Incompatible matrix dimensions"
    | otherwise = [[ sum $ zipWith (*) ar bc | bc <- transpose b ] | ar <- a]
  where
    transpose ([]:_) = []
    transpose x = (map head x) : transpose (map tail x)

-- Example usage
main :: IO ()
main = do
    let a = 1
        b = -3
        c = 2
    print $ quadraticRoots a b c

    let matrixA = [[1, 2, 3], [4, 5, 6]]
        matrixB = [[7, 8], [9, 10], [11, 12]]
    print $ matrixMultiply matrixA matrixB

    putStrLn "Hello, world"
    putStrLn "This is my first code in Haskell"
    putStrLn "I am learning Haskell"
