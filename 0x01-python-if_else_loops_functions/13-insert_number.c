#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - insert node in sorted list
 * @head: pointer to a pointer to the head of the list
 * @number: value to be inserted
 *
 * Return: Address of new node, NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *temp, *new;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	current = *head;
	temp = NULL;
	while ((current != NULL) && (current->n < number))
	{
		temp = current;
		current = current->next;
	}
	if (temp == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		temp->next = new;
		new->next = current;
	}

	return (new);
}
