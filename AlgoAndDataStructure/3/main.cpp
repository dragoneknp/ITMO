#include <iostream>
#include <string>


using namespace std;

pair<long, long> pairs[100000];
long n;

void siftUp(long i) {
    if (i != 0) {
        if (pairs[(i - 1) / 2].first > pairs[i].first) {
            swap(pairs[(i - 1) / 2], pairs[i]);
            siftUp((i - 1) / 2);
        }
    }
}

void siftDown(long i) {
    long left = 2 * i + 1;
    long right = 2 * i + 2;
    long j;
    if (right < n && pairs[right].first < pairs[i].first) {
        j = right;
    } else {
        j = i;
    }

    if (left < n && pairs[left].first < pairs[j].first) {
        j = left;


    }
    if (i != j) {
        swap(pairs[i], pairs[j]);
        siftDown(j);
    }
}

void push(long elem, long i) {
    n++;
    pairs[n - 1].first = elem;
    pairs[n - 1].second = i;
    siftUp(n - 1);

}

long extractMin() {
    long ans = pairs[0].first;
    swap(pairs[0], pairs[n - 1]);
    n--;
    siftDown(0);
    return ans;
}

long decreaseKey(long x, long y) {
    long i;
    for (i = 0; i < n; i++) {
        if (pairs[i].second == x) {
            break;
        }
    }
    pairs[i].first = y;
    siftUp(i);
}

int main() {
    string required;
    freopen("priorityqueue.in", "r", stdin);
    freopen("priorityqueue.out", "w", stdout);
    long i = 1;
    n = 0;
    while (cin >> required) {
        if (required == "push") {
            int value;
            cin >> value;
            push(value, i);
        }
        if (required == "extract-min") {
            if (n == 0) {
                cout << "*\n";
            } else {
                cout << extractMin() << endl;
            }

        }
        if (required == "decrease-key") {
            long x, y;
            cin >> x >> y;
            decreaseKey(x, y);

        }
        i++;
    }
}