import { Stack } from 'expo-router'

export default function RootLayout() {
  return (
    <Stack>
      <Stack.Screen name="screens/ChatScreen" options={{ title: 'Chat' }} />
      <Stack.Screen name="screens/DashboardScreen" options={{ title: 'Dashboard' }} />
      <Stack.Screen name="screens/SettingsScreen" options={{ title: 'Settings' }} />
    </Stack>
  )
}
