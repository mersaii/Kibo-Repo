const countSpacesInString = require('./count-spaces-in-string')

describe('countSpacesInString', () => { 
    it('should', () => { 
        expect(countSpacesInString("Hello, World!")).toBe(1);
        expect(countSpacesInString("This is a test string.")).toBe(4);
        expect(countSpacesInString("NoSpacesHere")).toBe(0);
        expect(countSpacesInString("  Two spaces at the start")).toBe(6);

    })
})
