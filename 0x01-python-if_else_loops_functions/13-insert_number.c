#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - This inserts a number into a sorted singly linked list.
 * @head: head of a list.
 * @number: index of the list where the new node is
 * added.
 *
 * Return: the address of the new node
 * or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node;
	listint_t *new_node;

	if (!head)
	{
		return (NULL);
	}

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
	{
		return (NULL);
	}

	new_node->n = number;
	if (!*head)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}

	current_node = *head;
	while (current_node->next && (*(current_node->next)).n < number)
	{
		current_node = current_node->next;
	}

	if (current_node == *head)
	{
		new_node->next = current_node;
		*head = new_node;
	}
	else
	{
		new_node->next = current_node->next;
		current_node->next = new_node;
	}
	return (new_node);
}
