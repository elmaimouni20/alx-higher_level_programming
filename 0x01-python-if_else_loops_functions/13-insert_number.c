#include "lists.h"

/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: head of linked list
 * @number: index to insert
 * Return: the address of the new node, or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *temp, *h;
int key;

h = malloc(sizeof(listint_t));
h->n = number;
h->next = NULL;
key = number;

if (*head == NULL || key < (*head)->n)
{
h->next = *head;
*head = h;
}
else
{
temp = *head;
while (temp->next != NULL && temp->next->n < key)
temp = temp->next;
h->next = temp->next;
temp->next = h;
}

return (*head);
}
