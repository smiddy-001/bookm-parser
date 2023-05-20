'use client'
// @refresh reset
// @ts-nocheck
// use client

import React, { useEffect, useState } from 'react';

const Clock = () => {
  const [date, setDate] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => {
      setDate(new Date());
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  const days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
  const day = date.getDay();
  const hour = date.getHours();
  const minute = date.getMinutes();
  const second = date.getSeconds();
  const ampm = hour >= 12 ? "PM" : "AM";

  let hour12 = hour % 12;
  hour12 = hour12 ? hour12 : 12;

  const dateDiff =
    Math.floor(
      (new Date().setHours(23, 59, 59, 999) - date.getTime()) / 86400000
    ) + 1;

  const getDateSuffix = (date: number) => {
    if (date >= 11 && date <= 13) {
      return "th";
    }
    switch (date % 10) {
      case 1:
        return "st";
      case 2:
        return "nd";
      case 3:
        return "rd";
      default:
        return "th";
    }
  };

  const getDateLabel = (date: number) => {
    const suffix = getDateSuffix(date);
    return `${date}${suffix}`;
  };

  return (
    <div className="clockcont">
      <div className="clock">
        <div className="calendar">
          {days.map((value, index) => (
            <Word key={value} value={value} hidden={index !== day} />
          ))}
          <Word value={getDateLabel(dateDiff)} />
        </div>
        <div className="row">
          <div className="hour">
            <Number value={hour12} />
            <Word value={":"} />
            <Number value={minute} />
            <Word value={":"} />
            <Number value={second} />
          </div>
          <div className="ampm">
            <Word value={ampm} />
          </div>
        </div>
      </div>
    </div>
  );
};

export const Number = ({ value = 0 }) => {
  const result = String(value).padStart(2, "0");
  return (
    <div className="digital">
      <p>88</p>
      <p>{result}</p>
    </div>
  );
};

export const Word = ({
  value,
  hidden = false,
}: {
  value: string;
  hidden?: boolean;
}) => {
  const getStyle = (): React.CSSProperties => {
    return {
      visibility: hidden ? "hidden" : "visible",
    };
  };
  return (
    <div className="digital">
      <p>{value}</p>
      <p style={getStyle()}>{value}</p>
    </div>
  );
};

export { Clock as default };

