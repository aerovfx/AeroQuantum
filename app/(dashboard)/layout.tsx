import { Sidebar } from "./_components/sidebar";

const DashboardLayout = ({ 
    children 
}: { 
    children: React.ReactNode; 
}) => {
  return (
    <div className="h-full">
      <div className="hidden md:flex h-full w-56 flex-col fixed inset-y-0 z-50">
        <Sidebar />
      </div>
      <div className="ml-56">
        {children}
    </div> {/* Đảm bảo nội dung chính không bị che bởi sidebar */}
    </div>
  );
}

export default DashboardLayout;