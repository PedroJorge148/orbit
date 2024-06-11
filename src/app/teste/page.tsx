'use client'

import { ChangeEvent, useState } from 'react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

export default function SolvePage() {
  const [a, setA] = useState(1);
  const [b, setB] = useState(0);
  const [c, setC] = useState(0);

  const handleChange = (setter: React.Dispatch<React.SetStateAction<number>>) => (e: ChangeEvent<HTMLInputElement>) => {
    setter(parseFloat(e.target.value));
  };

  const solveQuadratic =  (a: number, b: number, c: number): number[] => {
    const discriminant = b * b - 4 * a * c;
    if (discriminant < 0) return [];

    const root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
    const root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
    return [root1, root2];
  };

  const roots = solveQuadratic(a, b, c);

  const generateChartData = () => {
    const data = [];
    for (let x = -10; x <= 10; x += 0.5) {
      const y = a * x * x + b * x + c;
      data.push({ x, y });
    }
    return data;
  };

  const data = generateChartData();

  return (
    <div className="flex flex-col items-center p-4">
      <h1 className="text-2xl font-bold mb-4">Quadratic Solver</h1>
      <div className="flex space-x-2 mb-4 text-black">
        <input
          type="number"
          value={a}
          onChange={handleChange(setA)}
          className="border rounded p-2"
          placeholder="a"
        />
        <input
          type="number"
          value={b}
          onChange={handleChange(setB)}
          className="border rounded p-2"
          placeholder="b"
        />
        <input
          type="number"
          value={c}
          onChange={handleChange(setC)}
          className="border rounded p-2"
          placeholder="c"
        />
      </div>
      <div className="mb-4">
        <h2 className="text-xl font-bold">Roots</h2>
        {roots.length > 0 ? (
          <p>
            x₁ = {roots[0].toFixed(2)}, x₂ = {roots[1].toFixed(2)}
          </p>
        ) : (
          <p>No real roots</p>
        )}
      </div>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" stroke="#ccc" />
          <XAxis dataKey="x" label={{ value: 'X-axis', position: 'insideBottomRight', offset: -10 }} />
          <YAxis label={{ value: 'Y-axis', angle: -90, position: 'insideLeft', offset: -10 }} />
          <Tooltip />
          <Legend verticalAlign="top" height={36} />
          <Line type="monotone" dataKey="y" stroke="#8884d8" strokeWidth={2} dot={{ r: 3 }} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
};