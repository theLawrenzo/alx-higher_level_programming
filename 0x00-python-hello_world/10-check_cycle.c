#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - Check if a singly linked list has a cycle in it
 * @list: Head of the list
 *
 * Return: 0 if there is no cycle,
 * 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	int i;

	if (list->next == NULL)
		return (0);
	i = 0;
	while (list->next != NULL)
	{
		if (list->next == NULL && i)
			return (1);
		else
		{
			list = list->next;
		}
		i++;
	}
	return (0);
}
