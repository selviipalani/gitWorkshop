use std::env;
use log::{info};

fn fizzbuzz(up_limit: i32) {
    for up_limit in 1..up_limit + 1 {
        if is_divisible_by(up_limit, 3) {
            println!("Fizz");
        } else if is_divisible_by(up_limit, 5) {
            println!("Buzz");
        } else if is_divisible_by(up_limit, 15) {
            println!("Fizz Buzz");
        }
    }
}

// Function that returns a boolean value
fn is_divisible_by(lhs: i32, rhs: i32) -> bool {
    // Corner case, early return
    info!("{} % {}", lhs, rhs);
    if rhs == 0 {
        return false;
    }

    lhs % rhs == 0
}

fn main() {
    let args: Vec<String> = env::args().collect();
    println!("Size of the args: {}", args.len());
    if args.len() < 2 {
        fizzbuzz(10000);
    } else {
        let up_limit: i32 = (&args[1]).parse().unwrap();
        fizzbuzz(up_limit);
    }
}
