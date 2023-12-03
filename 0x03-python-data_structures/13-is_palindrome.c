#include "lists.h"
/**
 * is_palindrome - check if the list is palindrome
 * @head: the head of the list
 * Return: 0 if false 1 if true
 */
int is_palindrome(listint_t **head)
{
	if (head == 0 || *head == 0)
		return(1);
	return (ispalindrome(head, *head));
}

/**
 * ispalindrome - helps is_palindrome
 * @head: the head of the list
 * @end: the end of the list
 * Return: 0 if false 1 if true
 */
int ispalindrome(listint_t **head, listint_t *end)
{
	if (end == 0)
		return (1);
	if (ispalindrome (head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
