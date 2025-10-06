// Implementacao do algoritmo de ordenacao mergesort
#include "merge_sort.h"

// Função auxiliar para juntar dois subarrays ordenados
void merge(std::vector<std::string>& vec, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    std::vector<std::string> leftVec(n1), rightVec(n2);

    for (int i = 0; i < n1; i++)
        leftVec[i] = vec[left + i];
    for (int j = 0; j < n2; j++)
        rightVec[j] = vec[mid + 1 + j];

    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2) {
        if (leftVec[i] <= rightVec[j]) {
            vec[k] = leftVec[i];
            i++;
        } else {
            vec[k] = rightVec[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        vec[k] = leftVec[i];
        i++;
        k++;
    }

    while (j < n2) {
        vec[k] = rightVec[j];
        j++;
        k++;
    }
}

// Função recursiva do Merge Sort
void merge_sort_rec(std::vector<std::string>& vec, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        merge_sort_rec(vec, left, mid);
        merge_sort_rec(vec, mid + 1, right);
        merge(vec, left, mid, right);
    }
}

// Função principal chamada do Python
std::vector<std::string> merge_sort(std::vector<std::string> arr) {
    merge_sort_rec(arr, 0, arr.size() - 1);
    return arr;
}
