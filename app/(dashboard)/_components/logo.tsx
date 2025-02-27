import Image from "next/image";

export const Logo = () => {
    return (
        <div className="flex items-center justify-center h-16 w-16 bg-gray-800">
        <Image 
            src="/logo.png" 
            alt="Logo" 
            width={64} 
            height={64} />
        </div>
    );
    }