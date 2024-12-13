interface CardProps {
  name?: string;
  image?: string;
  description?: string;
}

export default function HabitCard({ name, image, description }: CardProps) {
  if (name && image && description) {
    return (
      <>
        <div>{name}</div>
        <div>{image}</div>
        <div>{description}</div>
      </>
    );
  } else {
    return <div>create new habit</div>;
  }
}
