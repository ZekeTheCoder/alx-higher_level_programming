#include "lists.h"

/**
 * reverse_list - reverses a linked list in place
 *
 * @head: pointer to the head of the linked list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * compare_lists - compares two linked lists
 *
 * @list1: first linked list
 * @list2: second linked list
 *
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 && list2)
	{
		if (list1->n != list2->n)
		{
			return (0);
		}
		list1 = list1->next;
		list2 = list2->next;
	}

	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * An empty list is considered a palindrome.
 *
 * @head: head of linked list
 *
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *middle = NULL;
	listint_t *prev_slow = NULL;
	int is_palindrome = 1;

	if (!head || !*head)
	{
		return (1);
	}

	while (fast && fast->next)
	{
		prev_slow = slow;
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast)
	{
		middle = slow;
		slow = slow->next;
	}

	prev_slow->next = NULL;
	reverse_list(&slow);

	is_palindrome = compare_lists(*head, slow);

	if (middle)
	{
		prev_slow->next = middle;
		middle->next = slow;
	}
	else
	{
		prev_slow->next = slow;
	}

	return (is_palindrome);
}
