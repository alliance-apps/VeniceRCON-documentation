## Logger

Logger is a simple way to communicate to the Webinterface,
you can communicate info messages, error messages or other

```typescript
export interface Logger {
  info(message: string): void
  warn(message: string): void
  error(message: string): void
}
```