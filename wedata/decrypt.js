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
const decryptQueryData = async encryptedHexString => {
    await initializeDecryption();
    const encryptedBytes = arrayFromHexString(encryptedHexString);
    memoryBuffer.set(encryptedBytes);
    const decryptedLength = wasmModule._decrypt(memoryBuffer.byteOffset, encryptedBytes.length);
    if (decryptedLength < 0) throw new Error("Decryption failed");
    const decryptedBytes = new Uint8Array(memoryBuffer.slice(0, decryptedLength));
    const decoder = new TextDecoder('utf-8');
    const decryptedString = decoder.decode(decryptedBytes);
    console.log(decryptedString);
    // return JSON.parse(decryptedString);
};

const data = 'ac0c6659bf884019c55ebef36e77c73758eeeba43e6936f1b45b57529bef292d529bde22ff8c101cf80a109adca87389811548f647accf27178f3c4486c7ff744c4bd6653ace88a46112666558bc39c24cef8a540786d668ab120449a33d6790690f267fca52faab0aa962e1c517207a8c3e94e5717a3036f26294547839f72f381235440dbcf2b683a2f67230319456baead8e1fa11ff7dcd2a5b92b281de44cacc21a42ed466186d43223081e19876690f267fca52faab0aa962e1c517207a8c3e94e5717a3036f26294547839f72f3b92def107edf9e2f2355ec74056a9f1baead8e1fa11ff7dcd2a5b92b281de441c7d7cdf2eb0ea164d9b7f1799c55a7f4ce3663fb9189bed04644dac6305d49b4a49404b5849c0ab252024364eda3f05364db2e02a8350535f6c2cceb9d8a6a86d57b368ad91d5abfeddee7bbb888cf4a258d6c40fb4deaadea0208bea3fcde1e0499a3cb9912203f251cdb998a048dbcce42a019681cb898c2cd68c8b1a62244a49404b5849c0ab252024364eda3f05364db2e02a8350535f6c2cceb9d8a6a86d57b368ad91d5abfeddee7bbb888cf4a258d6c40fb4deaadea0208bea3fcde110c1e5b594c0eaab7fbe64acfe26fe2e8c6f6bef45f238315951b6e690dec44e4a49404b5849c0ab252024364eda3f0550b5e7163c3550af15a0d5674d288002500fe28e06e20c34603b8026c3b8ac38df61e67c04d6c578dd3389296339c4e783f95ea158196b2e1701bf61b43a6bd87a2bc003903631cb23823016c0afd3966d74446ca0c2f1378dc1c667431dfc737309b0f26e88bda663cc32e1941259b74c4ce7f7743cf6daeccedd3cb3632f9610f0a0f4970fe8899f57db360047a3f49374cdcbd6ac6596d5898254b165e7093251ebf7e72fbf7ce505aa451eb9b8a0b30ff5066a09a8d6a5a4c452293c7083ad3b753aae887a68ee6a84ef3377b028c74d876fba5035ce4b2b17851b3f88fb1f6a4cc15f029d5634509a661ace90d687aaf52286a9a620b7d052c9d411ea22f59860d1950e87ab8f67bf8ab0cbcada7a2bc003903631cb23823016c0afd3966d74446ca0c2f1378dc1c667431dfc73765b50e086d6be2e2c81bb7a98cea8a54c4ce7f7743cf6daeccedd3cb3632f9610f0a0f4970fe8899f57db360047a3f4baf4e6e04b4dc90ec70ec4e20297b4b0a1a825ddb218d229b4fad29f7fb842a2b30ff5066a09a8d6a5a4c452293c70833510b04339f021b32fe1004c18054908c74d876fba5035ce4b2b17851b3f88fb1f6a4cc15f029d5634509a661ace90d687aaf52286a9a620b7d052c9d411ea22c92160f5f585721fd3e3acddef568d777a2bc003903631cb23823016c0afd3966d74446ca0c2f1378dc1c667431dfc73be8b46dab592aeae03caa7b676ae0c47a637d22de940297d0fe823a44b7f85831f6a4cc15f029d5634509a661ace90d6e7385995c805317238f697a73883df0c59650ec1fd2268e54ff61573da0785ba3fe82d0481b2b88f69b85390d001b790b820fb824d504794d50d64a8118f1695760035e4617bd482c2730d228f67b7108f9422fe8bacd3ef25c37234de607de94a49404b5849c0ab252024364eda3f05dc09439b9152056a56ff9f6924ff7de009429c7c677b7cbe7784f277688fee8705c6fd020c063cd12acd6e8b4f0b25c7405549aad3399888eac24e968f04f15c1914c5ca9beb0f371c88a8448c74a96f74a400112b99c639d1e8d36d6a47a2d64c4ce7f7743cf6daeccedd3cb3632f9610f0a0f4970fe8899f57db360047a3f49374cdcbd6ac6596d5898254b165e709f2e1048104f719a954904dbf09f595a9e46fa05374663ce449ef7bc19f4cb2ab977cba2b6c7548a79733fb0f2b6b02abaf11c24ae2b721a7f757e1bcef80c5f47ebea998c357735d4d258e870a8572e3ab4e060613b9a375a1965d6ff39f4a6802e5d05a2fbe6777812d500e6493001c9eff3ad078c598273bd503cec07bd8d97a2bc003903631cb23823016c0afd396f79f7b75fc6368d80be4ed71da5ebb622367a2e1f867314e3c8678ac6f0d2911d246da5cd780c4003e8a29b779c9850da3171cb0118f6cd80497895f7db1c5a763bb5fe8a4262a80c2ff55a8b27b9404666244563e147c4cec9da9d9b31abd6dcedd2fe7268b8dc65038c85c08caa073d83d28710d4040dd5c1adf16c5d43397a17e1ee3c4e5a4539d71e0abc4a283360c2085d3ca4c14818f977373697d9b20054022cb2028c18dce39e768fc99e4bf4c841ef1916eecc44f5ffbd3f265d0cd3ff28ac978238e0fe0ddc0b20539e0568fd267919a85b8581b2e31fbb4666d68a3384ee2123a50bfa2c2ea3fae1eea8f988d38460143935b568aeecd32907d5b0e8ecdc6cebce5be55874a984a73079063b62224c7a7dff1748dd2038773fdd8676653f959dc08fb41e766cc0ec007e121c1c72e62520c4c0f5758be3fc2f46b4d6c75ac1cfdb648c7bd3e5e257460d809ca7929361d115c93149689150bdd3220c76245e0cc353781454fe44df65cb4ef2cb821588c1e94e78caca2ed7cf154e84a78502a977970cd81ae30c14973b8de05cec8094a468c3df0703bd6ba3944ddbae00f5e0f2d81f4f73e54f6f64e12d1e3d704d07a051ac64a696bd9e58cc204514c267906256477692ade458b07a42fdb95dd2de7b6c07036b157fe2ffceb9f1598f6e03726680b26845bf211f2018017b2988ac86c3cd739476720a3cbc98dff2043ddd26377310aa0dba34d19bf'

// 使用示例
await decryptResponseData(data)
