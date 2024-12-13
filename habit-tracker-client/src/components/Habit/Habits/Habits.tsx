import { useState, useEffect, useContext } from "react";
import HabitCard from "../HabitCard";
import { UserContext } from "../../../context/UserContext";

export default function Habits() {
  const { token } = useContext(UserContext)!;
  const [habits, setHabits] = useState<Array<any>>();

  const fetchHabits = async () => {
    const requestOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + token,
      },
    };
    const response = await fetch(
      "http://127.0.0.1:8000/api/user/habits",
      requestOptions
    );
    if (!response.ok) {
      return null;
    } else {
      return await response.json();
    }
  };

  useEffect(() => {
    const loadData = async () => {
      try {
        const data = await fetchHabits(); // Fetch the data
        setHabits(data); // Update the state with the fetched data
        console.log(data);
      } catch (err) {
        console.log(err);
      }
    };

    loadData(); // Call the fetch function
  }, []);

  return (
    <>
      <div>
        {!habits
          ? "null"
          : habits.map((habit) => {
              return (
                <HabitCard
                  name={habit.habit.name}
                  description={habit.habit.description}
                  image={habit.habit.image}
                />
              );
            })}
        {habits?.length! >= 6 ? "" : <HabitCard />}
      </div>
    </>
  );
}
