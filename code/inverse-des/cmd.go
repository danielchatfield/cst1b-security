package main

import (
	"crypto/des"
	"fmt"
)

var (
	key = []byte{0x73, 0x65, 0x63, 0x52, 0x33, 0x74, 0x24, 0x3b} // secR3t$
	src = []byte{0x61, 0x20, 0x74, 0x65, 0x73, 0x74, 0x31, 0x32} // a test12
)

func main() {
	dst := make([]byte, 8)
	block, err := des.NewCipher(key)

	if err != nil {
		panic(err)
	}

	block.Encrypt(dst, src)
	fmt.Println(dst) // [55 13 238 44 31 180 247 165]

	// inverse key and src
	for i := 0; i < 8; i++ {
		key[i] = ^key[i]
		src[i] = ^src[i]
	}

	block, err = des.NewCipher(key)

	if err != nil {
		panic(err)
	}

	block.Encrypt(dst, src)
	fmt.Println(dst) // [200 242 17 211 224 75 8 90]
}
