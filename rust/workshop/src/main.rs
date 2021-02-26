use std::env;
use log::{info};

fn fizzbuzz(up_limit: i32) {
    // TODO Implement me!
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
    if args.len() < 2 {
        fizzbuzz(10000);
    } else {
        let up_limit: i32 = (&args[1]).parse().unwrap();
        fizzbuzz(up_limit);
    }
}
