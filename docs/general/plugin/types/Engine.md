## Engine

Internal useable functions for vurcon related data

```typescript
export interface Engine {
  /** this event gets emitted when frontend got variable changes */
  on(event: "varsChanged", callback: (data: VarsChangedEventProps) => void): this
  /** 
   * this will respond with a string of permissions a guid might have
   * it will only respond with data when the user has an account on vurcon
   * and connected his soldier with his vurcon account
   */
  requestPlayerPermissions(guid: string): Promise<string[]>
}
```