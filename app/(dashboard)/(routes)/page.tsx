import { Button } from '../../components/ui/button';
import React from 'react';

export default function Home() {
  return (
    <div>
      <h1>This is a protected Page</h1>
      <Button onClick={() => alert('Button clicked!')}>Click Me</Button>
    </div>
  );
}