'use client'

import { cn } from '@/lib/utils'
import Link, { LinkProps } from 'next/link'
import { usePathname } from 'next/navigation'
import { ReactNode } from 'react'
import { Button } from './ui/button'

interface NavLinkProps extends LinkProps {
  children: ReactNode
}

export function NavLink({ children, ...props }: NavLinkProps) {
  const pathname = usePathname()

  return (
    <Button variant="link" size="xs" asChild className="justify-start">
      <Link
        data-current={pathname === props.href}
        className={cn(
          'flex gap-1.5 font-medium text-muted-foreground hover:text-foreground data-[current=true]:text-foreground data-[current=true]:underline',
        )}
        {...props}
      >
        {children}
      </Link>
    </Button>
  )
}
