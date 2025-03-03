import cipher from "../js/cipher";

// write your unit tests here

describe('cipher.encode()', () => {
    it('should encode a message with a valid offset', () => {
        const result = cipher.encode('HELLO', 3);
        expect(result).toBe('KHOOR');
    });

    it('should handle lowercase letters', () => {
        const result = cipher.encode('hello', 3);
        expect(result).toBe('KHOOR');
    });

    it('should handle uppercase letters', () => {
        const result = cipher.encode('KHOOR', 3);
        expect(result).toBe('NKRRU');
    });

    it('should handle spaces', () => {
        const result = cipher.encode('HELLO WORLD', 3);
        expect(result).toBe('KHOOR ZRUOG');
    });

    it('should handle offsets at the upper limit (26)', () => {
        const result = cipher.encode('HELLO', 26);
        expect(result).toBe('HELLO');
    });

    it('should handle offsets at the lower limit (1)', () => {
        const result = cipher.encode('HELLO', 1);
        expect(result).toBe('IFMMP');
    });

});

describe('cipher.decode()', () => {
    it('should decode a message with a valid offset', () => {
        const result = cipher.decode('KHOOR', 3);
        expect(result).toBe('HELLO');
    });

    it('should handle lowercase letters', () => {
        const result = cipher.decode('khoor', 3);
        expect(result).toBe('HELLO');
    });

    it('should handle uppercase letters', () => {
        const result = cipher.decode('KHOOR', 3);
        expect(result).toBe('HELLO');
    });

    it('should handle spaces', () => {
        const result = cipher.decode('KHOOR ZRUOG', 3);
        expect(result).toBe('HELLO WORLD');
    });

    it('should handle offsets at the upper limit (26)', () => {
        const result = cipher.decode('HELLO', 26);
        expect(result).toBe('HELLO');
    });

    it('should handle offsets at the lower limit (1)', () => {
        const result = cipher.decode('IFMMP', 1);
        expect(result).toBe('HELLO');
    });
});
