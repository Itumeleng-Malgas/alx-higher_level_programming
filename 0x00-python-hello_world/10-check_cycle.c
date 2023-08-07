#include "lists.h"

/**
 * check_cycle - function checks for a cycle in a singly linked.
 * @list: first node pointer.
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);
	slow = list;
	fast = slow->next;

	while (slow != NULL && fast->next != NULL
		&& fast->next->next != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}

