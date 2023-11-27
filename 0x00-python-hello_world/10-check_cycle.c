#include "lists.h"
/**
 * chech_cycle - checks it is cyclical
 * @list: pointer to list
 * Return: 1 if cyclical, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return(0);
}
