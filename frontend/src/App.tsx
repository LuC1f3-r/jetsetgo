import { Routes, Route, Link } from 'react-router-dom';
import Flights from './components/Flights';
import Hotels from './components/Hotels';
import Cars from './components/Cars';

export default function App() {
  return (
    <div className="p-6 font-sans">
      <nav className="flex gap-4 mb-6">
        <Link to="/flights" className="text-blue-500">Flights</Link>
        <Link to="/hotels" className="text-blue-500">Hotels</Link>
        <Link to="/cars" className="text-blue-500">Cars</Link>
      </nav>

      <Routes>
        <Route path="/flights" element={<Flights />} />
        <Route path="/hotels" element={<Hotels />} />
        <Route path="/cars" element={<Cars />} />
      </Routes>
    </div>
  );
}
