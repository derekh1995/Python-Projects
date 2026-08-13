I made this rock paper scissors game utilizing multiple nested conditional statements, lists, pseudorandom number generation (PRNG), and I wrapped it all in a while-loop. 
Initially, there was no while-loop, but I got tired of continuously having to restart the program to play again, so I looped it.
After I implemented the loop, I discovered that the outcomes no longer changed for my choices; this was due to my PRNG variable being placed outside of the loop. I moved it inside the loop and it worked correctly again.
