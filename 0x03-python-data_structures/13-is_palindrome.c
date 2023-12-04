#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * An empty list is considered a palindrome
 *
 * @head: head of linked list
 *
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *list_head = *head;
	int nodes = 0, i = 0;
	int index, *arr;

	if (!head || !*head)
	{
		return (1);
	}

	while (list_head)
	{
		nodes++;
		list_head = list_head->next;
	}

	arr = malloc(sizeof(int) * nodes);
	list_head = *head;

	while (list_head)
	{
		arr[i] = list_head->n;
		list_head = list_head->next;
		i++;
	}

	index = nodes - 1;

	for (i = 0; i <= index; i++)
	{
		if (arr[i] != arr[index])
		{
			return (0);
		}
		index--;
	}

	free(arr);
	return (1);
}
