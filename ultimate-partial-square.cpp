#include <iostream>
#include <fstream>
#include <chrono>

using namespace std;



int main(){
    std::chrono::time_point<std::chrono::high_resolution_clock> start = std::chrono::high_resolution_clock::now();
    long int limit = 44444;//20;
    int digits[limit]; 
    digits[0] = 5;
    

    int carry_old = 0;
    int current_length = 1;
    int found_digit = 5;

    while(current_length < limit){

        if(current_length % 1000 == 0){
            std::cout << current_length << '\n';
        }

        digits[current_length] = 0;

        int carry_new = 0;
        long long value_a = 0;
        int value_b = 0;
        int j = 0;
        for (int i=1; i<((current_length>>1) + 1); i++){
            j = current_length-i;
            int temp_a = digits[i] * digits[j];
            if (i!=j){
                temp_a += temp_a;
            }
            value_a += temp_a;
        }

        carry_new += value_a / 10;
        value_a = value_a % 10;

        if (current_length > 1){
            value_b = (5 * found_digit) / 5;
        }else{
            value_b = (5 * found_digit) / 10;
        }

        int t_result = value_a + value_b + carry_old;
        found_digit = t_result % 10;
        digits[current_length] = found_digit;
        
        carry_old = carry_new + (t_result / 10);

        current_length ++;
    }

    ofstream myfile;
    myfile.open ("result.txt");
    for (int i=current_length-1; i>=0; i--){
        myfile << digits[i];
        cout << digits[i];
    }
    myfile.close();

    cout<<endl;
    std::chrono::time_point<std::chrono::high_resolution_clock> finish = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = finish - start;
    std::cout << "Elapsed time: " << elapsed.count() << " s\n";

    return 0;
}
