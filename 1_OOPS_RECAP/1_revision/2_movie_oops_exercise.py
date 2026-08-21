class Movie:
    def __init__(self, movie_name: str, total_seats: int = 100, ticket_price: int = 500) -> None:
        self.movie_name: str = movie_name
        self.total_seats: int = total_seats
        self.ticket_price: int = ticket_price
        self.booked_seats: int = 0

    def book_ticket(self, num_tickets: int) -> str:
        if num_tickets <= (self.total_seats - self.booked_seats):
            self.booked_seats += num_tickets
            return f"Ticket booked. Total amount to pay: {self.ticket_price * num_tickets} Rs."
        else:
            return f"Sorry, not enough seats available."

    def show_status(self) -> str: 
        return f"movie name: {self.movie_name}, total seats available: {self.total_seats - self.booked_seats}, total seats booked: {self.booked_seats}"

movie: Movie = Movie("Krish", 100, 499)
print(movie.show_status())
print(movie.book_ticket(70))
print(movie.show_status())
print(movie.book_ticket(70))


