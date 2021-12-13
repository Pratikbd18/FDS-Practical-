#include <iostream>
using namespace std;


class Stack{
    public:
        char l[50], top;
        int lenth;

    Stack(){
        lenth = 0;
    }

    void push(char c){
        l[lenth] = c;
        lenth += 1;
        top = c;
    }

    void pop(){
        lenth -= 2;
        top = l[lenth];
        lenth += 1;
    }
};

int main(){
    Stack s;
    char word[5];
    char res[5];
    cout<<"Enter the word: ";
    cin>>word;
    for (int i = 0; i < 5; i++)
    {
        s.push(word[i]);
    }

    for (int i = 0; i < 5; i++)
    {   
        res[i] = s.top;
        cout<<s.top;
        s.pop();
    }
    
    cout<<endl<<"Its ";

    for (int i = 0; i < 5; i++)
    {   
        if (res[i] != word[i])
        {
            cout<<" not a palindrome";
            break;
        }
    }
    cout<<" a palindrome";
}