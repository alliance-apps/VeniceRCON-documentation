## PluginStore

a store to save simple data in order to persist over plugin restarts

```typescript
export interface PluginStore {
  /** sets data to the store which can be retrieved via .get */
  set(key: string, value: any): void
  /** retrieves data by a certain key which has been set via the .save function */
  get(key: string): any
  /** resets the store */
  clear(): void
}
```