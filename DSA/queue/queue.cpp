#include <iostream>
#include <vector>
using namespace std;

class Queue {
private:
    vector<int> items;

public:
        bool is_empty(){
            return items.empty();
        }

        void enqueue( int value ){
            items.push_back(value);
        }

        void dequeue(){
            if ( is_empty() ){
                cout << "Queue is empty" << endl;
                return ;
            }
            else {
                items.erase( items.begin() );
            }
        }

        void display_queue(){
            if ( is_empty() ){
                cout << "Queue is empty" << endl;
            }
            else {
                for ( int item : items ){
                    cout << item << " " ;
                }
                cout << endl;
            }
        }
};

int main(){
    Queue q;
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.enqueue(40);
    q.display_queue();
    q.dequeue();
    q.dequeue();
    q.display_queue();
    return 0;
}
