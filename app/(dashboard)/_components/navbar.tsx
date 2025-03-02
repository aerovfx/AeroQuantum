import { NavbarRoutes } from '@/components/navbar.routes';

import { MobileSidebar }    from './mobile-sidebar';

export const Navbar = () => {
    return (
        <div className="p-4 border-b h-full flex items-center bg-white shadow-sm">
            <NavbarRoutes />
            <MobileSidebar />
        </div>
    )
}
// Compare this snippet from app/%28dashboard%29/_components/navbar-routes.tsx:
// "use client";
//
//
//  