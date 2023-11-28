#include "lists.h"
#include <stddef.h>
/**
 * insert_node - insert a number in a linked list based on its value
 * @head: the head of the list
 * @number: the number to be inserted
 * Return: node on success
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new = malloc(sizeof(listint_t));

	if (new == 0)
		return (0);
	new->n = number;
	new->next = 0;
	if (!node || new->n < node->n)
	{
		new->next = node;
		return (*head = new);
	}
	while (node)
	{
		if (!node->next || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	return (0);
}
