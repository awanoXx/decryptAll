let wasmModule = null,
    decryptionPromise = null,
    memoryBuffer = new Uint8Array(0);

const reset = () => {
    wasmModule = null;
    decryptionPromise = null;
};

const hexStringFromArray = t => Array.from(t).map(t => t.toString(16).padStart(2, "0")).join("");

const initializeDecryption = () => {
    return new Promise(resolve => {
        if (!decryptionPromise) {
            decryptionPromise = new Promise(resolve => {
                (async function() {
                    try {
                        if (!wasmModule) {
                            wasmModule = await window.__decrypt_initWasm__();
                            memoryBuffer = allocateMemory(2e6);
                        }
                        resolve(true);
                    } catch (e) {
                        console.error(e);
                        resolve(false);
                    }
                })();
            });
        }
        resolve(decryptionPromise);
    });
};

const hexToUint8Array = (array, hexString, length) => {
    for (let i = 0; i < length; i++) {
        array[i] = parseInt(hexString.substr(2 * i, 2), 16);
    }
};
const allocateMemory = size => {
    const ptr = wasmModule._malloc(size);
    return new Uint8Array(wasmModule.HEAPU8.buffer, ptr, size);
};

const arrayFromHexString = hexString => {
    const result = [];
    for (let i = 0; i < hexString.length; i += 2) {
        result.push(parseInt(hexString.substr(i, 2), 16));
    }
    return new Uint8Array(result);
};
// 解密返回数据
const decryptResponseData = async hexString => {
    await initializeDecryption();
    const byteLength = Math.ceil(hexString.length / 2);
    const byteArray = allocateMemory(byteLength);
    hexToUint8Array(byteArray, hexString, byteLength);
    const decryptedLength = wasmModule._decrypt(byteArray.byteOffset, byteLength);
    if (decryptedLength < 0) throw new Error("Decryption failed");
    const decryptedString = wasmModule.UTF8ToString(byteArray.byteOffset, decryptedLength);
    wasmModule._free(byteArray.byteOffset);
    try {
        return decryptedString;
    } catch (error) {
        return decryptedString;
    }
};

// 解密请求数据
const decryptRequestData = async (hexString) => {
    // 反转十六进制字符串
    const reversedHexString = hexString.match(/.{2}/g).reverse().join('');
    
    // 直接将十六进制转换为字符串
    const decodedString = reversedHexString.match(/.{2}/g)
        .map(hex => String.fromCharCode(parseInt(hex, 16)))
        .join('');
    
    try {
        return JSON.parse(decodedString);
    } catch (error) {
        return decodedString;
    }
};
const data = '7d2268636e75616c223a22626174222c312d3a226e6f6973726576222c313a22796164227b'

// 使用示例
await decryptRequestData(data)
