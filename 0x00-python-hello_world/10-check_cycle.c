#include "lists.h"

/**
 * find_cycle_start - finds the starting point of the cycle.
 *
 * @list: pointer to the head of the list
 * @collision: the meeting point of the pointers
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */
int find_cycle_start(listint_t *list, listint_t *collision)
{
	listint_t *slow = list;

	while (slow != collision)
	{
		slow = slow->next;
		collision = collision->next;
	}

	return (1);
}

/**
 * check_cycle - checks if a singly linked list has a
 * cycle in it
 *
 * @list: pointer to the head of the list
 *
 *  Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (find_cycle_start(list, slow));
		}
	}

	return (0);
}
