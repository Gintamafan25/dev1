export interface Fighters {
    "id": number,
    "first_name": string,
    "initial": string,
    "last_name": string,
}

export interface User {
    "id": number,
    "username": string
}

export interface Register {
    "username": string,
    "email": string,
    "password": string,
    "confirm_password": string
}
export interface CookieMap {
    [key: string]: string
}

export interface Response {
    "message": string
}