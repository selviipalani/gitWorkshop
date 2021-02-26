use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let up_limit = &args[1];
    println!("{0}", up_limit);
}
