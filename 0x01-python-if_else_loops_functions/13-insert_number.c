#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - add node at the beginning of a listint_t list
 * @head: Pointer to the head element of the list
 * @number: Number to include in new node
 *
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current, *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	current = *head;
	if (*head == NULL)
		*head = new;
	else
	{
		while ((current->next != NULL) && (number > current->n))
		{
			prev = current;
			current = current->next;
		}

		new->next = current;
		prev->next = new;
	}
	return (new);
}
