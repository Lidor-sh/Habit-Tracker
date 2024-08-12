interface Promps {
  className: string;
  id: string;
  children: React.ReactNode;
}

export default function Section({ className, id, children }: Promps) {
  return (
    <>
      <div id={id} className={`${className} SectionContainer`}>
        {children}
      </div>
    </>
  );
}
