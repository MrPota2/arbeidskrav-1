use std::io;
use std::time::Instant;
use std::hint::black_box;

fn main() {

    println!("Please enter a positive integer: ");
    let mut selected_number = String::new();

    io::stdin()
        .read_line(&mut selected_number)
        .expect("Failed to read line");
        
    let int_value: u32 = selected_number
        .trim()
        .parse()
        .expect("The selected number is not a positive integer");
        
    let int_value = black_box(int_value as u128);
    
    println!("Number {} selected.", int_value);
    
    let start = Instant::now();
    let mut sum_of_number_range_loop: u128 = int_value;
    for i in 0..int_value {
        sum_of_number_range_loop += i;
    }
    let elapsed_loop = start.elapsed();
    
    let start = Instant::now();
    let sum_of_number_range_div: u128 = int_value * (int_value + 1) / 2;
    let elapsed_div = start.elapsed();
    
    println!("Loop: The sum of all numbers from 0 to {} is {}. - Calculated in {:#?}", int_value, sum_of_number_range_loop, elapsed_loop);
    println!("Base 10 division: The sum of all numbers from 0 to {} is {}. - Calculated in {:#?}", int_value, sum_of_number_range_div, elapsed_div);
}
